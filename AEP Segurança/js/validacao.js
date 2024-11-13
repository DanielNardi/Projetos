var codigo

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
  const dados = { cpf: cpf };
  var respostaAPI;
  try{
    const response = await fetch('http://127.0.0.1:4000/mandar_codigo', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(dados),
    });
    respostaAPI = await response.json(); 
  } catch (error) {
    console.error('Erro ao enviar dados:', error);
  }
  console.log(respostaAPI)
  codigo = respostaAPI['Mensagem'];
}

chamar();

function botao(){

  const input = document.getElementById('verificar').value;

  if(codigo == input){
    window.alert('Código correto! Você será mandado para o site.');
    window.location.href = '../html/banco.html';
  }else{
    window.alert('Seu código está errado! Tente novamente.')
  }
  
}