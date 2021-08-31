import Card from "../components/Card/Card";
import React from 'react';
import AppContext from '../context';

function Favorites({ onAddToFavorite, onPlus }) {
  
  const {favorites} = React.useContext(AppContext);
  
  return (
    <div className="content p-40">
      <div className="d-flex align-center justify-between mb-40 ">
        <h1 className="">Мои закладки</h1>
      </div>

      <div className="d-flex flex-wrap">
        {favorites.map((card) => (
          <Card
            // onPlus={onAddToCart}
            // onFavorite={onAddToFavorite}
            key={card.id}
            favorited={true}
            onFavorite={onAddToFavorite}
            onPlus={onPlus}
            {...card}
          />
        ))}
      </div>
    </div>
  );
}

export default Favorites;
