from sqlalchemy.orm import declarative_base, Session
from sqlalchemy.orm import relationship
from sqlalchemy import Column, func
from sqlalchemy import select
from sqlalchemy import create_engine
from sqlalchemy import inspect
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey


Base = declarative_base()


class User(Base):
    __tablename__ = "user_account"

    # attributes
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)

    address = relationship(
        "Address", back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, fullname={self.fullname})"


class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True)
    email_address = Column(String(30), nullable=False)
    user_id = Column(Integer, ForeignKey("user_account.id"), nullable=False)

    user = relationship("User", back_populates="address")

    def __repr__(self):
        return f"Address(id={self.id}, email_address={self.email_address})"


print(User.__tablename__)
print(Address.__tablename__)

# conexão com o banco de dados
engine = create_engine("sqlite://")

# criando classes como tabela no banco de dados
Base.metadata.create_all(engine)

# depreciado - sera removido em futuro release
# print(engine.table.names())

# investiga o esquema de banco de dados
inspetor_engine = inspect(engine)
print(inspetor_engine.has_table("user_account"))
print(inspetor_engine.get_table_names())
print(inspetor_engine.default_schema_name)

with Session(engine) as session:
    emerson = User(
        name="emerson",
        fullname="Emerson Ricardo",
        address=[Address(email_address='emerson@gmail.com')]

    )

    teste = User(

        name='test_1',
        fullname='teste_001',
        address=[Address(email_address='teste_001@gmail.com'),
                 Address(email_address='teste_0001@gmail.com.org')]

    )

    # associando usuario sem e-mail
    teste_02 = User(

        name='test_2',
        fullname='teste_002'

    )
    # enviando para o BD (persistência de dados)
    session.add_all([emerson, teste, teste_02])

    session.commit()

stmt = select(User).where(User.name.in_(['emerson']))
print("\nRecuperando usuarios a partir de condição de filtragem! ")
for user in session.scalars(stmt):
    print(user)

# retornando e-mails
stmt_address = select(Address).where(Address.user_id.in_([2]))
print("\nRecuperando os endereços de e-mail  ")
for address in session.scalars(stmt_address):
    print(address)


# recuperando informações
stmt_order = select(User).order_by(User.fullname.desc())
print("\nRecuperando dados de forma ordenada!")
for result in session.scalars(stmt_order):
    print(result)

stmt_join = select(User.fullname, Address.email_address).join_from(Address, User)
print('\n')
for result in session.scalars(stmt_join):
    print(result)

connection = engine.connect()
results = connection.execute(stmt_join).fetchall()
print("\nExecutando statement a partir da conexão!")
for result in results:
    print(result)


stmt_count = select(func.count('*')).select_from(User)
print("\nTotal de instancias em User")
for result in session.scalars(stmt_count):
    print(result)

