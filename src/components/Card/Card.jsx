import React from "react";
import styles from "./Card.module.scss";
import ContentLoader from "react-content-loader";

function Card(props) {
  const [isAdded, setIsAdded] = React.useState(props.added);
  const [isFavorite, setIsFavorite] = React.useState(props.favorited);

  const onClickPlus = () => {
    setIsAdded(!isAdded);
    props.onPlus({
      title: props.title,
      price: props.price,
      image_url: props.image_url,
      id: props.id,
    });
  };
  const onClickFavorite = () => {
    setIsFavorite(!isFavorite);
    props.onFavorite({
      title: props.title,
      price: props.price,
      image_url: props.image_url,
      id: props.id,
    });
  };

  return (
    <div className={styles.card}>
      {props.loading ? (
        <ContentLoader
          speed={2}
          width={155}
          height={190}
          viewBox="0 0 150 190"
          backgroundColor="#f3f3f3"
          foregroundColor="#ecebeb"
          {...props}
        >
          <rect x="0" y="0" rx="10" ry="10" width="150" height="90" />
          <rect x="0" y="105" rx="10" ry="10" width="150" height="15" />
          <rect x="0" y="135" rx="10" ry="10" width="100" height="15" />
          <rect x="0" y="165" rx="10" ry="10" width="80" height="25" />
          <rect x="115" y="155" rx="10" ry="10" width="35" height="35" />
        </ContentLoader>
      ) : (
        <>
          <div className={styles.favorite} onClick={onClickFavorite}>
            <img
              src={
                isFavorite ? "/img/heart-liked.svg" : "/img/heart-unliked.svg"
              }
              alt="Unliked"
            />
          </div>
          <img width={133} height={112} src={props.image_url} alt="Sneakers" />
          <h5>{props.title}</h5>
          <div className="d-flex justify-between align-center">
            <div className="d-flex flex-column">
              <span>Цена: </span>
              <b>{props.price} руб.</b>
            </div>

            <img
              className={styles.plus}
              src={isAdded ? "/img/btn-checked.svg" : "/img/btn-unchecked.svg"}
              alt="Plus"
              onClick={onClickPlus}
            />
          </div>
        </>
      )}
    </div>
  );
}

export default Card;
