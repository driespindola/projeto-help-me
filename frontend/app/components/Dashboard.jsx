import { Box, Button, Card, Container } from '@mui/material';
import React,{useState,useEffect} from 'react';

function Dashboard() {
  const [data,setData]=useState([]);
  const getData=()=>{
    fetch('data.json'
    ,{
      headers : { 
        'Content-Type': 'application/json',
        'Accept': 'application/json'
       }
    }
    )
      .then(function(response){
        console.log(response)
        return response.json();
      })
      .then(function(myJson) {
        console.log(myJson);
        setData(myJson)
      });
  }
  useEffect(()=>{
    getData()
  },[])

  return (
    <Container  sx={{ 
        display: 'flex', 
        flexDirection: 'column', 
        textAlign: 'center', 
        justifyContent: 'center', 
        alignItems: 'center',
        padding: 5 
    }}>
        <h1>Solicitações</h1>
        <Box sx={{display: 'grid', gridTemplateColumns: 'auto auto'}}>
            {
            data && data.length>0 && data.map((item)=>
            <Card sx={{ margin: 2, padding: 5, width: 400 }}>
            <p><b>Nome: </b>{item.nome}</p>
            <p><b>Tipo de Solicitação:</b> {item.tipo}</p>
            <p><b>Gravidade:</b> {item.gravidade}</p>
            <p><b>Descrição:</b> {item.descricao}</p>
            </Card>
            )
            }
        </Box>
     <Box>
        <Button href='/solicitacao' variant="contained">Fazer Solicitação</Button>
     </Box>
    </Container>
    
  );
}

export default Dashboard;