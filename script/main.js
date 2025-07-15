document.getElementById('button').onclick = async function () {
      const tamanho = document.getElementById('length').value;
      const maiusculas = document.getElementById('uppercase').checked;
      const numeros = document.getElementById('numbers').checked;
      const simbolos = document.getElementById('symbols').checked;

      try {
        const resposta = await fetch('http://localhost:5000/gerar_senha', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            tamanho: Number(tamanho),
            maiusculas,
            numeros,
            simbolos
          })
        });

        const dados = await resposta.json();
        document.getElementById('password').value = dados.senha || dados.erro || 'Erro ao gerar senha';
      } catch (e) {
        document.getElementById('password').value = 'Erro de conexão com o backend';
      }
    };