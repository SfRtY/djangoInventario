function cambiarParrafos()
{
  var lista=document.getElementsByTagName('p');
  for(var x=0;x<lista.length;x++){
      lista[x].childNodes[0].nodeValue=lista[x].childNodes[0].nodeValue + "."
  }  
}   