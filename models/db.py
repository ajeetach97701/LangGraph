from Libs.libs import *


class VectorDB(Enum):
    CHROMA = "chroma"
    MILVUS = "milvus"
    
    
class StoreArguments(BaseModel):
    path: str = Field(
        ..., description="List of dictionaries containing data to store. Each dictionary should have a 'content' key with the actual content."
    )
    collection_name: str = Field(
        ..., description="Name of the collection to store the data in. Follows the format 'general_store_<id>'."
    )
    store_type: VectorDB = Field(
        ... , description="Type of vector store to use. "
    )
    embeddings:OpenAIEmbeddings = Field(..., description='embedding to be provided to vector store ')
    

class VectorStore:
    """
Initializes a VectorStore instance with the provided store arguments.

Parameters:
    **kwargs (StoreArguments): Arbitrary keyword arguments for configuring the VectorStore.
"""
    def __init__(self, **kwargs:StoreArguments):
        """
        Initializes a VectorStore instance with the provided store arguments.

        Parameters:
            **kwargs (StoreArguments): Arbitrary keyword arguments for configuring the VectorStore,
            including 'store_type', 'path', 'collection_name', and 'embeddings'.
        """
        self.store_type  = kwargs.get('store_type', None)
        self.path: str =kwargs.get('path')
        self.collection_name: str =  kwargs.get('collection_name',None)
        self.embeddings = kwargs.get('embeddings')
        self.docs = []

        
    def create_document(self, max_chunk_size:int= 100):
        """
Creates documents from a file specified by the path attribute, supporting CSV, PDF, and JSON formats.

Parameters:
    max_chunk_size (int): Maximum size for chunks when processing JSON files. Default is 100.

Returns:
    list: A list of Document objects created from the file content.
    str: An error message if the file type is unsupported or an exception occurs.
"""
        # To get the file path (csv, pdf, json only works for now)
        file_type = self.path.split(".")[-1]
        csv_docs = []
        if file_type == "csv":
            loader = CSVLoader(self.path)
            csv_data = loader.load_and_split()
            for i in range(len(csv_data)):
                csv_docs.append(Document(page_content=csv_data[i].page_content))
            return csv_docs
        
        elif file_type == "pdf":
            pdf_docs =[]
            loader = PyMuPDFLoader(self.path)
            pdf_data = loader.load_and_split()
            for i in range(len(pdf_data)):
                pdf_docs.append(Document(page_content=pdf_data[i].page_content))
            
            return pdf_docs
            
        elif file_type == "json":
            json_docs = []
            try:
                with open(self.path, "r") as f:
                    docs_json = json.load(f)
                splitter = RecursiveJsonSplitter(max_chunk_size=max_chunk_size)
                splited_json = splitter.split_json(docs_json)
                json_documents = splitter.create_documents(splited_json,)
                for i in range(len(json_documents)):
                    json_docs.append(Document(page_content=json_documents[i].page_content))
                    json_docs = json_docs + [Document(page_content=json_documents[i].page_content)]
                    
                return json_docs
            except Exception as e:
                return e
            
        else:
            return f"file type error. Allowed file types are .csv, .pdf, .json only "  

    def create_vector_store(self,max_chunk_size:int= 100):
        """
    Creates a vector store based on the specified store type.

    Parameters:
        max_chunk_size (int): Maximum size for chunks when processing JSON files. Default is 100.

    Returns:
        dict: A response dictionary containing the status and collection name if successful.
        Exception: An exception object if an error occurs during the process.

    Raises:
        Exception: If an error occurs during the creation of the vector store.
    """
        try:
            if self.store_type ==VectorDB.MILVUS:
                splits = self.create_document(max_chunk_size=max_chunk_size)
                vectorstore_milvus=Milvus.from_documents(embedding=self.embeddings, 
                                                            documents=splits, connection_args = connection_args,
                                                            collection_name=self.collection_name)
                response={"status": "success",
                        "type": "Milvus",
                        "collection_name":self.collection_name
                        }
                return response
                # return vectorstore_milvus

            elif self.store_type == VectorDB.CHROMA:
                # try:

                    splits = self.create_document()  
                    from langchain_chroma import Chroma
                    vectorstore_chroma = Chroma.from_documents(documents = splits, embedding=self.embeddings, persist_directory=f"./Chroma/{self.collection_name}_Chroma")

                    message = f"Chroma of the name {self.collection_name} has been updated."
                    response = {"status": message, "collection name":os.getenv("GENERAL_HYUNDAI")}
                    if vectorstore_chroma:
                        return response
        except Exception as e:
            return e
    def get_vector_store(self):
        """
    Retrieves the vector store based on the specified store type.

    Returns:
        Milvus or Chroma: An instance of the vector store configured with the specified
        embeddings and collection name, depending on the store type.
        Exception: An exception object if an error occurs during retrieval.

    Raises:
        Exception: If an error occurs during the retrieval of the vector store.
    """
        print("----------------------\n",connection_args,"\n-----------------------")
        try:

            if self.store_type == VectorDB.MILVUS:
                
                vectorstore=Milvus(embedding_function=self.embeddings,
                                    connection_args = connection_args,collection_name=self.collection_name)
                
                
                return vectorstore

            elif self.store_type == VectorDB.CHROMA:
                from langchain_chroma import Chroma
                collection_name = self.collection_name
                vectorstore = Chroma(embedding_function=self.embeddings,persist_directory=f"./Chroma/{collection_name}_Chroma")
                return vectorstore
            else:
                print("The vector store you are looking for does not exist. Please create a new one or correct the collection name of the vector store")
        except Exception as e :
            return e
        
