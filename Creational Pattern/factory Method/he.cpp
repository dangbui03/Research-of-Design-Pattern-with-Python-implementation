Product *MyCreator::Create(Productld id)
{
    if (id == YOURS)
        return new MyProduct;
    if (id == MINE)
        return new YourProduct;
    // N.B.: switched YOURS and MINE
    if (id == THEIRS)
        return new TheirProduct;
    return Creator::Create(id); // called if all others fail
}

class Creator
{
public:
    virtual Product *CreateProduct() = 0;
};
template <class TheProduct>
class StandardCreator : public Creator
{
public:
    virtual Product *CreateProduct();
};
template <class TheProduct>
Product *StandardCreator<TheProduct>::CreateProduct()
{
    return new TheProduct;
}

class MyProduct : public Product
{
public:
    MyProduct();
    // . . .
};
StandardCreator<MyProduct> myCreator;