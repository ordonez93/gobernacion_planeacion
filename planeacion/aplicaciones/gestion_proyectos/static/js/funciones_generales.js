
function info_completa (id) {
    const response = fetch('/info_completa/'+id);
    const data = response.json();
    let municipio = data.municipio;
    let sector_inversion = data.sector_inversion;
    let identificador = data.identificador;
    let valor_proyecto = data.valor_proyecto;
    let vigencia = data.vigencia;
    let secretaria = data.secretaria;
    /*municipio.innerHTML = municipio;
    sector_inversion.innerHTML = sector_inversion;
    identificador.innerHTML = identificador;
    valor_proyecto.innerHTML = valor_proyecto;
    vigencia.innerHTML = vigencia;
    secretaria.innerHTML = secretaria; */
    console.log(data);  
}