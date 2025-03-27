from matplotlib import pyplot as plt


plt.style.use('ggplot')

eixo_x_meses = [1, 5, 10, 15, 20, 25, 30]
eixo_y_produtoA = [28, 29, 25, 32, 34, 36, 31]
eixo_y_produtoB = [21, 22, 17, 23, 23, 24, 20]

plt.plot(eixo_x_meses, eixo_y_produtoA, linestyle='-', marker='o')
plt.plot(eixo_x_meses, eixo_y_produtoB, linestyle='--', marker='^')

plt.title('Vendas dos Produtos')
plt.xlabel('Meses')
plt.ylabel('Vendas')
plt.legend(['Produto A', 'Produto B'])

plt.grid()

plt.show()