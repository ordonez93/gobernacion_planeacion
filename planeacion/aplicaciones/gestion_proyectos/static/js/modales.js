
const ModalEditar = new bootstrap.Modal(
  document.getElementById("editar-registro"),
  {}
);
function EditarRegistro(id, nombre) {
  ModalEditar.show();
  var nombre_actual = document.getElementById("nombre-registro");
  nombre_actual.innerHTML = nombre;
  var id_registro = document.getElementById("id-registro");
  id_registro.value = id;
  var nombre_r = document.getElementById("nuevo-nombre");
  nombre_r.value = nombre;
}


const ModalEliminar = new bootstrap.Modal(
  document.getElementById("eliminar-registro"),
  {}
);
function EliminarRegistro(id, nombre) {
  ModalEliminar.show();
  var nombre_actual = document.getElementById("registro-eliminar");
  nombre_actual.innerHTML = nombre;
  var id_registro = document.getElementById("id-eliminar");
  id_registro.value = id;
}
