async function chamar(){
  event.preventDefault();

  const nome = document.getElementById('name').value;
  const data = document.getElementById('birthdate').value;
  const cpf = document.getElementById('cpf').value;
  const email = document.getElementById('email').value;
  const senha = document.getElementById('password').value;

  const dados = { nome: nome,data_nascimento: data, cpf: cpf, email: email, senha: senha };

  var respostaAPI;

  try{
    const response = await fetch('http://127.0.0.1:4000/cadastro', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(dados),
    });
    respostaAPI = await response.json(); 
    console.log(respostaAPI);
  } catch (error) {
    console.error('Erro ao enviar dados:', error);
  }

  console.log(respostaAPI)

  if (respostaAPI['Mensagem'] == true){
    window.alert('Sua conta foi criada! Vá para a área de login.')
  } else{
    window.alert('Sua conta já existe! Tente fazer o login.')
  }
}