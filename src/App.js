import React from "react";
import axios from "axios";

import { Route } from "react-router-dom";
import AppContext from "./context";
import "./App.scss";

import Header from "./components/Header";
import Drawer from "./components/Drawer";
import Home from "./pages/Home";
import Favorites from "./pages/Favorites";


function App() {
  const [items, setItems] = React.useState([]);
  const [cartItems, setCartItems] = React.useState([]);
  const [favoriteItems, setFavoriteItems] = React.useState([]);
  const [searchValue, setSearchValue] = React.useState("");
  const [cartOpened, setCartOpened] = React.useState(false);
  const [isLoading, setIsLoading] = React.useState(true);

  React.useEffect(() => {
    async function fetchData() {
      setIsLoading(true);
      const itemsResponse = await axios.get("/api/sneakers");
      const cartResponse = await axios.get("/api/cart");
      const favoriteResponse = await axios.get("/api/favorite");

      let sneakers = itemsResponse.data.sneakers;
      let cartItemsId = cartResponse.data.cart.map((obj) => obj.item_id);
      let favoriteItemsId = favoriteResponse.data.favorite.map(
        (obj) => obj.item_id
      );

      setIsLoading(false);

      setCartItems(
        sneakers.filter((item) => cartItemsId.indexOf(item.id) !== -1)
      );
      setFavoriteItems(
        sneakers.filter((item) => favoriteItemsId.indexOf(item.id) !== -1)
      );
      setItems(sneakers);
    }

    fetchData();
  }, []);

  const onAddToCart = (obj) => {
    if (cartItems.find((item) => item.id === obj.id)) {
      axios.delete(`/api/cart/${obj.id}`);
      setCartItems((prev) => prev.filter((item) => item.id !== obj.id));
    } else {
      axios.post("/api/cart", { item_id: obj.id });
      setCartItems((prev) => [...prev, obj]);
    }
  };

  const onAddToFavorite = (obj) => {
    if (favoriteItems.find((item) => item.id === obj.id)) {
      axios.delete(`/api/favorite/${obj.id}`);
      setFavoriteItems((prev) => prev.filter((item) => item.id !== obj.id));
    } else {
      axios.post("/api/favorite", { item_id: obj.id });
      setFavoriteItems((prev) => [...prev, obj]);
    }
  };

  const onRemoveItem = (id) => {
    axios.delete(`/api/cart/${id}`);
    setCartItems((prev) => prev.filter((item) => item.id !== id));
  };

  // const onRemoveFavoriteItem = (id) => {
  //   axios.delete(`/api/favorite/${id}`);
  //   setFavoriteItems((prev) => prev.filter((item) => item.id !== id));
  // };

  const onSearchInput = (event) => {
    setSearchValue(event.target.value);
  };

  const onClear = () => {
    setSearchValue("");
  };
  return (
    <AppContext.Provider value={{items, favorites: favoriteItems, cartItems}}>
      <div className="wrapper clear">
        {cartOpened && (
          <Drawer
            onClose={() => setCartOpened(false)}
            items={cartItems}
            onRemove={onRemoveItem}
          />
        )}
        <Header onClickCart={() => setCartOpened(true)} />

        <Route path="/" exact>
          <Home
            items={items}
            searchValue={searchValue}
            onClear={onClear}
            onSearchInput={onSearchInput}
            onAddToCart={onAddToCart}
            onAddToFavorite={onAddToFavorite}
            cartItems={cartItems}
            isLoading={isLoading}
          />
        </Route>

        <Route path="/favorites">
          <Favorites
            onAddToFavorite={onAddToFavorite}
            onPlus={onAddToCart}
          />
        </Route>
      </div>
    </AppContext.Provider>
  );
}

export default App;
