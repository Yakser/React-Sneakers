function Drawer({ onClose, items = [] }) {
  return (
    <div className="overlay">
      <div className="drawer">
        <h2 className="mb-30 d-flex justify-between">
          Корзина{" "}
          <img
            className="cu-p"
            src="/img/btn-remove.svg"
            alt="Remove"
            onClick={onClose}
          />
        </h2>
        <div className="items flex">
          {items.map((item) => (
            <div className="cartItem d-flex align-center mb-20" key={item.title}>
              <div
                className="cartItemImg"
                style={{ backgroundImage: `url(${item.image_url})` }}
              ></div>
              <div className="mr-20 flex">
                <p className="mb-5">{item.title}</p>
                <b>{item.price} руб.</b>
              </div>
              <img
                className="removeBtn"
                src="/img/btn-remove.svg"
                alt="Remove"
              />
            </div>
          ))}
        </div>
        <div className="cartTotalBlock">
          <ul>
            <li>
              <span>Итого:</span>
              <div></div>
              <b>21 498 руб. </b>
            </li>
            <li>
              <span>Налог 5%: </span>
              <div></div>
              <b>1074 руб. </b>
            </li>
          </ul>
          <button className="greenButton">
            Оформить заказ <img src="/img/arrow.svg" alt="Arrow" />
          </button>
        </div>
      </div>
    </div>
  );
}
export default Drawer;
