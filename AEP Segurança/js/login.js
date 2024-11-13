async function chamar(){
  event.preventDefault();

  const email = document.getElementById('email').value;
  const senha = document.getElementById('password').value;

  const dados = { email: email, senha: senha };

  var respostaAPI;

  try{
    const response = await fetch('http://127.0.0.1:4000/login', {
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

  if (respostaAPI['Mensagem'] != '0'){
    window.alert('Você realizou o login com sucesso!')
    let data = new Date();
    data.setTime(data.getTime() + (1 * 24 * 60 * 60 * 1000));
    let expira = "expires=" + data.toUTCString();
    document.cookie = "cpf" + "=" + encodeURIComponent(respostaAPI['Mensagem']) + ";" + expira + ";path=/"; 
    window.location.href = '../html/validacao.html';

  } else{
    window.alert('Está conta não existe.')
  }
}