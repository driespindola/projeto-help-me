import React from 'react'
import { Button, Container, Box, FormControl, FormLabel, Input } from '@mui/material'

const Home = () => {
  return (
    <Container sx={{ 
      display: 'flex', 
      flexDirection: 'column', 
      textAlign: 'center', 
      justifyContent: 'center', 
      alignItems: 'center' 
    }}>
      <h1>Login</h1>
      <Box sx={{ display: 'flex', flexDirection: 'column', width: 200 }}>
        <FormControl >
          <FormLabel form="text" sx={{ textAlign: 'left' }}>Nome Completo:</FormLabel>
          <Input type="text" placeholder='Nome'></Input>
          <FormLabel forn="text" sx={{ textAlign: 'left', marginTop: 3 }}>Senha:</FormLabel>
          <Input type="password" placeholder="Senha"></Input>
          <Button variant="contained" sx={{ margin: 3 }}>Login</Button>
        </FormControl>
      </Box>
      <Box >
        <p>Novo por aqui? <Button href='/cadastro' variant="contained">Cadastre-se</Button></p>
      </Box>
    </Container>
  )
}

export default Home