import React from "react";
import axios from "axios";
import "./App.scss";
import Card from "./components/Card/Card";
import Header from "./components/Header";
import Drawer from "./components/Drawer";

function App() {
  const [items, setItems] = React.useState([]);
  const [cartItems, setCartItems] = React.useState([]);
  const [searchValue, setSearchValue] = React.useState("");
  const [cartOpened, setCartOpened] = React.useState(false);

  React.useEffect(() => {
    axios.get("/api/sneakers").then((res) => setItems(res.data.sneakers));
    axios.get("/api/cart").then((res) => {
      let cartItemsId = res.data.cart.map((obj) => obj.item_id);

      setCartItems(items.filter((item) => cartItemsId.indexOf(item.id) !== -1));
      // setCartItems(items.filter((item) => cartItemsId.includes(item.id)));
      console.log(items.filter(item => cartItemsId.indexOf(item.id) !== -1));
    })
  
  }, []);

  const onAddToCart = (obj) => {
    // cartItems.includes(obj)
    //   ? setCartItems((prev) => [...prev].splice(prev.findIndex(obj), 1))
    axios.post("/api/cart", {item_id: obj.id});
    setCartItems((prev) => [...prev, obj]);
  };

  const onSearchInput = (event) => {
    setSearchValue(event.target.value);
  };

  const onClear = () => {
    setSearchValue("");
  };
  return (
    <div className="wrapper clear">
      {cartOpened && (
        <Drawer onClose={() => setCartOpened(false)} items={cartItems} />
      )}
      <Header onClickCart={() => setCartOpened(true)} />

      <div className="content p-40">
        <div className="d-flex align-center justify-between mb-40 ">
          <h1 className="">
            {searchValue
              ? `Поиск по запросу: "${searchValue}"`
              : "Все кроссовки"}
          </h1>
          <div className="search-block d-flex align-center">
            <img src="/img/search.svg" alt="Search" />
            {searchValue && (
              <img
                className="cu-p clear"
                src="/img/clear.svg"
                alt="Clear"
                onClick={onClear}
              />
            )}
            <input
              type="text"
              placeholder="Поиск..."
              value={searchValue}
              onChange={onSearchInput}
            />
          </div>
        </div>

        <div className="d-flex flex-wrap">
          {items
            .filter((item) =>
              item.title.toLowerCase().includes(searchValue.toLowerCase())
            )
            .map((card) => (
              <Card
                key={card.id}
                title={card.title}
                price={card.price}
                image_url={card.image_url}
                onPlus={onAddToCart}
                onFavorite={() => {
                  console.log("123");
                }}
              />
            ))}
        </div>
      </div>
    </div>
  );
}

export default App;
