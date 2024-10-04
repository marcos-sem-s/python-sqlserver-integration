CREATE TABLE produtos (
	codigo_produto VARCHAR(20) NOT NULL PRIMARY KEY, 
	nome_produto VARCHAR(50), 
	embalagem VARCHAR(50), 
	tamanho VARCHAR(50), 
	sabor VARCHAR(50), 
	preco_lista SMALLMONEY
);
