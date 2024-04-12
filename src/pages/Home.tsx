import { useNavigate } from "react-router-dom";

export default function Home() {
  const nav = useNavigate();

  const onChange = (e) => {
    const value = e.target.value;
    console.log("onChange", value);
    nav(`/${value}`);
  };

  return (
    <>
      <h1 className="text-3xl font-bold underline text-red-50">Home Page</h1>
      <select
        className="select select-bordered w-full max-w-xs"
        onChange={onChange}
      >
        <option disabled selected>
          Change page here
        </option>
        <option value="about">Go About</option>
        <option value="contact">Go Contact</option>
      </select>
    </>
  );
}
