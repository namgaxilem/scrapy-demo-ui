import { useState } from "react";
import { NavLink } from "react-router-dom";

export default function Notification() {
  const [keyValue, setKeyValue] = useState("");
  const [inputValue, setInputValue] = useState("");

  const onSaveLC = () => {
    if (keyValue) {
      localStorage.setItem(keyValue, inputValue);
      setInputValue("");
      setKeyValue("");
    }
  };

  return (
    <>
      <div className="flex flex-col gap-3">
        <label>
          key
          <input
            value={keyValue}
            onChange={(e) => setKeyValue(e.target.value)}
          />
        </label>

        <label>
          value
          <input
            value={inputValue}
            onChange={(e) => setInputValue(e.target.value)}
          />
        </label>

        <button onClick={onSaveLC}>Save to localStorage</button>
      </div>

      <NavLink to={"/about"}>Go check localStorage</NavLink>
    </>
  );
}
