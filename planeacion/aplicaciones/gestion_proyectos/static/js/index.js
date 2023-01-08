window.addEventListener('load',async()=>{
    let id = document.getElementById('id_usuario').value;
    const response = await fetch('/cantidad_asignaciones/'+id);
    const data = await response.json();
    let cantidad = data.cantidad;
    if (cantidad > 0) {
      cant.innerHTML = cantidad;
       
    }
    else{
        cant.style.visibility = 'hidden';
        }
    
  });