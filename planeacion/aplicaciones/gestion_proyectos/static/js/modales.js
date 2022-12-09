
const myModal = new bootstrap.Modal(
  document.getElementById("editar-registro"),
  {}
);
function ModalEditar(id, nombre) {
  myModal.show();
  var nombre_actual = document.getElementById("nombre-registro");
  nombre_actual.innerHTML = nombre;
  var id_registro = document.getElementById("id-registro");
  id_registro.value = id;
  var nombre_r = document.getElementById("nuevo-nombre");
  nombre_r.value = nombre;
}
