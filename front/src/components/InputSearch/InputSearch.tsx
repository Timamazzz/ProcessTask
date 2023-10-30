import React, { FC, useState } from "react";
import FormInput from "../FormInput/FormInput";
import Buttons from "../Buttons/Buttons";
import "./styles.scss";

interface InputSearchProps {
  items: string[]; // Массив элементов для поиска
}

const InputSearch: FC<InputSearchProps> = ({ items }) => {
  const [searchTerm, setSearchTerm] = useState("");
  const [searchResults, setSearchResults] = useState<string[]>([]);
  const [isSearching, setIsSearching] = useState(false);

  const handleSearch = () => {
    setIsSearching(true);
    const searchText = searchTerm.toLowerCase();
    const filtered = items.filter((item) =>
      item.toLowerCase().includes(searchText)
    );
    setSearchResults(filtered);
    setIsSearching(false);
  };

  return (
    <div className="inputSearchContainer">
      <FormInput
        style="searchInput"
        value={searchTerm}
        onChange={(e) => setSearchTerm(e)}
        subInput={undefined}
        placeholder="Введите слово для поиска…"
        required={false}
        error={false}
        keyData={""}
        friedlyInput={false}
      />

      <Buttons
        className="buttonSearch"
        text={"Поиск"}
        onClick={() => handleSearch()}
      />
    </div>
  );
};

export default InputSearch;
