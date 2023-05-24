from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column, Session
from sqlalchemy import Column, Integer, String, ForeignKey, Table, create_engine


engine = create_engine('sqlite:///database.db', echo=True)
session = Session(bind=engine)


class Base(DeclarativeBase):
    __abstract__ = True

    def __str__(self):
        return f"<{self.__class__.__name__} {self.__dict__}>"


class Cliente(Base):
    __tablename__ = 'cliente'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(50))
    password: Mapped[str] = mapped_column(String(50))

    def __repr__(self) -> str:
        return f"<Cliente(id={self.id}, name={self.name}, email={self.email}, password={self.password})>"


class Categoria(Base):
    __tablename__ = 'categoria'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(String(50))

    def __repr__(self) -> str:
        return f"<Categoria(id={self.id}, name={self.name}, description={self.description})>"


class Produto(Base):
    __tablename__ = 'produto'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(String(50))
    price: Mapped[str] = mapped_column(String(50))
    category_id: Mapped[int] = mapped_column(
        Integer, ForeignKey('categoria.id'))

    def __repr__(self) -> str:
        return f"<Produto(id={self.id}, name={self.name}, description={self.description}, price={self.price}, category_id={self.category_id})>"


many_carrinho_produto = Table('carrinho_produto', Base.metadata, Column(
    'carrinho_id', Integer, ForeignKey('carrinho.id')), Column('produto_id', Integer, ForeignKey('produto.id')))


class Carrinho(Base):
    __tablename__ = 'carrinho'
    id: Mapped[int] = mapped_column(primary_key=True)
    cliente_id: Mapped[int] = mapped_column(Integer, ForeignKey('cliente.id'))
    produtos: Mapped[list] = relationship(
        'Produto', secondary=many_carrinho_produto, backref='carrinho')

    def __repr__(self) -> str:
        return f"<Carrinho(id={self.id}, cliente_id={self.cliente_id}, produtos={self.produtos})>"


# Criar banco de dados
# Base.metadata.create_all(engine)

if __name__ == '__main__':
    # Criar banco de dados
    session = Session(bind=engine)
    # Get all clientes
    clientes = session.query(Cliente).all()
    print(clientes)
