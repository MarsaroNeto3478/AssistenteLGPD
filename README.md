# Assistente LGPD (nome provisório)

## O QUE É?
Projeto criado com foco em aprendizado e estudo, utilizando IA para melhor desenvolvimento.

Resumo: O projeto é um RAG que contém pdfs com a regras e artigos da LGPD (Lei Geral de Proteçao de Dados Pessoais), focado em auxiliar pessoas que estão com dúvidas sobre leis, normas, boas práticas.


# MEU ESTUDO:
Essa sessão será para o meu estudo, o que estou aprendendo com o projeto, novos conteúdos, ou conteúdos já vistos mas com a intenção de reforçar o que já foi visto.

## RAG

### O que é um RAG:

Antes de falar sobre RAG é necessário explicar o problema por trás: Agentes de IA como ChatGPT ou Claude, aprendem com quantidade enorme de dados durante seu treinamento, após isso  o conhecimento "congela":
Isso gera alguns problemas:
- Desatualização: não sabe o que acontece após o treinamento;
- Não conhece o que é privado: ele nunca leu o manual de sua empresa, seus contratos, anotações;
- Alucinação: quando ele não sabe responder, ele inventa uma resposta que soa convincente, mas na verdade não é a resposta certa.

Analogia: aluno numa prova sem consultas. Ele pode usar o que memorizou. Se cair uma pergunta que ele não saiba, ele chuta ela com confiança.

Com isso, veio a solução: Transformar a prova sem consulta numa com consulta.
RAG (Retrival Augmented Generation/Geração Aumentada por Recuperação):
R = Ele busca informações relevantes em uma base de documentos;
A = Coloca as informações junto com a pergunta;
G = a IA escreve usando esse material.

Analogia: aluno numa prova com consulta. Ele pode ler no "livro", encontrar a página certa e responder com base nela.

## Na prática:
Na criação do RAG temos duas partes:
- Fase 1: Preparação: Feita apenas uma vez:
	- A) Documentos: Aqui vamos montar a base de dados, o "livro" para ela olhar: PDFs, manuais, textos...
	- B) Pedaços(Chunks): Aqui, dividimos/cortamos os textos em chunks, partes menores, de alguns parágrafos cada: Uma analogia é fazer fichas de resumo sobre cada assunto para a prova, é mais eficiente achar a ficha certa, em comparação de folhear várias páginas até achar a página certa; 
	- C) Embeddings: 
	- D)
