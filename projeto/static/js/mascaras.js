$(document).ready(function() {
    $('#id_cpf').mask('000.000.000-00', {reverse: false});
    $('.mask-cnpj').mask('00.000.000/0000-00', {reverse: false});
    $('#id_cep').mask('00000-000', {reverse: false});
    $('#id_identidade').mask('00.000.000', {reverse: false});
    $('#id_celular').mask('(00) 00000-0000');
    $('#id_data_habilitacao').mask('00/00/0000', {reverse: false});
    $('#id_data_cadastro').mask('00/00/0000', {reverse: false});
    $('#id_data_nascimento').mask('00/00/0000', {reverse: false});
});

$('#signup-modal').on('hide.bs.modal', function(event) {
    if ($(this).find('.is-invalid').length > 0) {
        event.preventDefault(); // Impede o fechamento do modal se houver campos inválidos
    }
});