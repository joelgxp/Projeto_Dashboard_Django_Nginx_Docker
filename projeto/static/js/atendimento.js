document.getElementById('openModalBtn').addEventListener('click', function() {
    document.getElementById('exameModal').style.display = 'block';
  });
  
  document.getElementsByClassName('close')[0].addEventListener('click', function() {
    document.getElementById('exameModal').style.display = 'none';
  });
  
  document.getElementById('exameForm').addEventListener('submit', function(event) {
    event.preventDefault();
    // Aqui você pode pegar os valores dos campos e realizar alguma ação, como enviar para um servidor
    const nomeExame = document.getElementById('nomeExame').value;
    const tipoSolicitacao = document.getElementById('tipoSolicitacao').value;
    const valorExame = document.getElementById('valorExame').value;
  
    console.log('Nome do Exame:', nomeExame);
    console.log('Tipo de Solicitação:', tipoSolicitacao);
    console.log('Valor do Exame:', valorExame);
  
    // Aqui você pode adicionar lógica para enviar os dados para o servidor ou fazer o que desejar com eles
    // Por exemplo, você pode enviar uma requisição AJAX para uma API que irá lidar com o cadastro do exame
  
    // Fechar o modal após enviar os dados
    document.getElementById('exameModal').style.display = 'none';
  });


  function openModalWithId(id) {
    // Abra o modal aqui, usando a lógica de exibição do modal

    // Exemplo:
    document.getElementById('exameModal').style.display = 'block';

    // Você pode fazer qualquer ação adicional aqui com o ID recebido
    console.log("ID do paciente:", id);

    document.getElementsByClassName('close')[0].addEventListener('click', function() {
      document.getElementById('exameModal').style.display = 'none';
    });
}
  