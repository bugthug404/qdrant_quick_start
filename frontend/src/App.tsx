import React from "react";
import axios from "axios";

function App() {
  const buttonClass =
    "mx-auto px-4 py-2 bg-blue-200 rounded-full cursor-pointer";

  async function calling(path: string) {
    try {
      const response = await axios.get(`http://localhost:3009/${path}`);
      console.log(response.data.data);
    } catch (error) {
      console.log(error);
    }
  }

  return (
    <>
      <div className=" h-screen justify-center flex flex-col gap-4 items-center">
        <div className="p-4 bg-gray-100 rounded-3xl max-w-sm w-full flex flex-wrap gap-4">
          <div
            className={buttonClass}
            onClick={() => {
              calling("search/add-books");
            }}
          >
            Add Books
          </div>
          <div
            className={buttonClass}
            onClick={() => {
              calling("search/search-books?query=alien%20invasion");
            }}
          >
            Search Books
          </div>
        </div>
        <div className="p-4 bg-gray-100 rounded-3xl max-w-sm w-full flex flex-wrap gap-4">
          <div
            className={buttonClass}
            onClick={() => {
              calling("create-collection");
            }}
          >
            Create Collection
          </div>
          <div
            className={buttonClass}
            onClick={() => {
              calling("query-collection");
            }}
          >
            Query Collection
          </div>
          <div
            className={buttonClass}
            onClick={() => {
              calling("dynamic-query-collection");
            }}
          >
            Dynamic Query Collection
          </div>
        </div>
      </div>
    </>
  );
}

export default App;
