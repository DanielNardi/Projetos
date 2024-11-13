async function chamar(){

  function getCookie(cpf) {
    const CPF = cpf + "=";
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
        let cookie = cookies[i].trim(); 
        if (cookie.indexOf(CPF) === 0) {
            return decodeURIComponent(cookie.substring(CPF.length, cookie.length)); 
        }
    }
    return null;
  }
  const cpf = getCookie("cpf");
  var respostaAPI;
  url = 'http://127.0.0.1:4000/listar/'+ cpf 
  try{
    const response = await fetch(url, {
      method: 'GET',
    });
    respostaAPI = await response.json(); 
  } catch (error) {
    console.error('Erro ao enviar dados:', error);
  }
  console.log(respostaAPI)
  pessoa = respostaAPI['Mensagem'];

  document.getElementById('nome_usuario').textContent = pessoa['nome'];
  document.getElementById('email_usuario').textContent = pessoa['email'];
  document.getElementById('valor_na_conta').textContent = '17.593,12';
  document.getElementById('numero_cartao_debito').textContent = '1234 5678 9012 3456';
  document.getElementById('cvv_debito').textContent = '123';
  document.getElementById('nome_usuario_cartao_debito').textContent = pessoa['nome'];
  document.getElementById('data_validade_debito').textContent = '12/24';
  
  document.getElementById('numero_cartao_credito').textContent = '9876 5432 1098 7654';
  document.getElementById('cvv_credito').textContent = '456';
  document.getElementById('nome_usuario_cartao_credito').textContent = pessoa['nome'];
  document.getElementById('data_validade_credito').textContent = '11/25';
  document.getElementById('valor_limite_cartao').textContent = '3.000,00';

}

chamar();
