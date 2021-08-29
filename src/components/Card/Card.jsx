import styles from './Card.module.scss';

function Card(props) {
    const onPlusBtnClick = () => {
       
    }
    return (
      <div className={styles.card}>
        <div className={styles.favorite}>
          <img src="/img/heart-unliked.svg" alt="Unliked" />
        </div>
        <img width={133} height={112} src={props.imageUrl} alt="Sneakers" />
        <h5>{props.title}</h5>
        <div className="d-flex justify-between align-center">
          <div className="d-flex flex-column">
            <span>Цена: </span>
            <b>{props.price} руб.</b>
          </div>
          <button className="button" onClick={onPlusBtnClick}>
            <img src="/img/plus.svg" alt="Plus" width={11} height={11} />
          </button>
        </div>
      </div>
    );
}

export default Card;