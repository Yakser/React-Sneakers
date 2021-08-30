import React from 'react';
import styles from "./Card.module.scss";

function Card(props) {

    const [isAdded, setIsAdded] = React.useState(false);

    const onClickPlus = () => {
      setIsAdded(!isAdded);
      props.onPlus({title: props.title, price: props.price, image_url: props.image_url});
    }
    return (
      <div className={styles.card}>
        <div className={styles.favorite} onClick={props.onFavorite}>
          <img src="/img/heart-unliked.svg" alt="Unliked" />
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
      </div>
    );
}

export default Card;