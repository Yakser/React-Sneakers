import Card from "../components/Card/Card";

function Home({
  searchValue,
  onClear,
  onSearchInput,
  onAddToCart,
  onAddToFavorite,
  items,
  cartItems,
  isLoading,
}) {
  const renderItems = () => {
    return (
      isLoading
        ? [...Array(12)]
        : items.filter((item) =>
            item.title.toLowerCase().includes(searchValue.toLowerCase())
          )
    ).map((card, index) => (
      <Card
        key={index}
        onPlus={onAddToCart}
        onFavorite={onAddToFavorite}
        added={cartItems.some((obj) => obj.id === card.id)}
        loading={isLoading}
        {...card}
      />
    ));
  };

  return (
    <div className="content p-40">
      <div className="d-flex align-center justify-between mb-40 ">
        <h1 className="">
          {searchValue ? `Поиск по запросу: "${searchValue}"` : "Все кроссовки"}
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

      <div className="d-flex flex-wrap">{renderItems()}</div>
    </div>
  );
}

export default Home;
