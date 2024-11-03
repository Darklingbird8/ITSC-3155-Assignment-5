@app.post("/order_details/", response_model=schemas.OrderDetail, tags=["OrderDetails"])
def create_orderdetail(orderdetail: schemas.OrderDetailCreate, db: Session = Depends(get_db)):
    return order_details.create(db=db, orderdetail=orderdetail)


@app.get("/order_details/", response_model=list[schemas.OrderDetail], tags=["OrderDetails"])
def read_order_details(db: Session = Depends(get_db)):
    return order_details.read_all(db)


@app.get("/order_details/{orderdetail_id}", response_model=schemas.OrderDetail, tags=["OrderDetails"])
def read_one_orderdetail(orderdetail_id: int, db: Session = Depends(get_db)):
    orderdetail = order_details.read_one(db, orderdetail_id=orderdetail_id)
    if orderdetail is None:
        raise HTTPException(status_code=404, detail="User not found")
    return orderdetail


@app.put("/order_details/{orderdetail_id}", response_model=schemas.OrderDetail, tags=["OrderDetails"])
def update_one_orderdetail(orderdetail_id: int, orderdetail: schemas.OrderDetailUpdate, db: Session = Depends(get_db)):
    orderdetail_db = order_details.read_one(db, orderdetail_id=orderdetail_id)
    if orderdetail_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    return order_details.update(db=db, orderdetail=orderdetail, orderdetail_id=orderdetail_id)


@app.delete("/order_details/{orderdetail_id}", tags=["OrderDetails"])
def delete_one_orderdetail(orderdetail_id: int, db: Session = Depends(get_db)):
    orderdetail = order_details.read_one(db, orderdetail_id=orderdetail_id)
    if orderdetail is None:
        raise HTTPException(status_code=404, detail="User not found")
    return order_details.delete(db=db, orderdetail_id=orderdetail_id)