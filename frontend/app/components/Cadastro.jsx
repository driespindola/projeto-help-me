import { Box, Button, Container, FormControl, FormGroup, FormHelperText, Input, InputLabel, MenuItem, TextField } from '@mui/material'
import React, { useState } from 'react'

const Cadastro = () => {
    const [nome, setNome] = useState('')
    const [codigo, setCodigo] = useState(0)
    const [senha, setSenha] = useState('')
    const [confirmarSenha, setConfirmarSenha] = useState('')
    const [color, setColor] = useState('')
    const [errorTextName, setErrorTextName] = useState('')
    const [errorTextPassword, setErrorTextPassword] = useState('')
    const [errorName, setErrorName] = useState(false)
    const [errorPassword, setErrorPassword] = useState(false)

    const codigos = [
        {
          value: '1000',
          label: 'area de TI',
        },
        {
          value: '1001',
          label: 'area de RH',
        },
        {
          value: '1002',
          label: 'area de Comércio',
        },
        {
          value: '1003',
          label: 'area Fiscal',
        },
        {
          value: '1004',
          label: 'area de Marketing',
        },
      ];

      const handleChange = (e) => {
        setCodigo(e.target.value);
      };

    function handleSubmit(e) {
        if (nome === '') {
            setErrorName(true)
            setErrorTextName('Nome não pode ficar em branco')
        } else if (nome.length < 4) {
            setErrorName(true)
            setErrorTextName('Nome deve haver mais de 4 characteres!')
        } else {
            setErrorName(false)
            setErrorTextName('')
        }
        if (senha !== confirmarSenha) {
            setErrorPassword(true)
            setErrorTextPassword('Senhas não coicidem')
        } else if (senha.length < 5) {
            setErrorPassword(true)
            setErrorTextPassword('Senha invalida, a senha requer um minimo de 5 caracteres nescessarios')
        } else if (senha.length > 20) {
            setErrorPassword(true)
            setErrorTextPassword('Senha invalida, a senha ultrapassa o limite de caracteres permitidos')
        } else {
            setErrorPassword(false)
            setErrorTextPassword('')
        }
    }

    
  return (
    <Container  sx={{ 
        display: 'flex', 
        flexDirection: 'column', 
        textAlign: 'center', 
        justifyContent: 'center', 
        alignItems: 'center' 
      }}>
        <h1>Cadastro</h1>
        <Box sx={{ display: 'flex', flexDirection: 'column', width: 400 }}>
            <FormGroup onSubmit={handleSubmit} >
                <FormControl >
                    <InputLabel error={errorName} form='text'>Nome Completo:</InputLabel>
                    <Input error={errorName} type='text' placeholder='Insira seu nome aqui' value={nome} onChange={(e) => setNome(e.target.value)} />
                    <FormHelperText error={errorName}>{errorTextName}</FormHelperText>
                </FormControl>
                <FormControl sx={{ marginTop: 5 }}>
                <TextField
                    select
                    label="Area"
                    value={codigos}
                    onChange={handleChange}
                >
                    {codigos.map((option) => (
                        <MenuItem key={option.value} value={option.value}>
                            {option.label}
                        </MenuItem>
                        ))}
                </TextField>
                </FormControl>
                <FormControl error={errorPassword} sx={{ marginTop: 5 }}>
                    <InputLabel error={errorPassword} form='password'>Senha:</InputLabel>
                    <Input type='password' placeholder='Insira sua senha aqui' value={senha} onChange={(e) => setSenha(e.target.value)} />
                    <FormHelperText error={errorPassword}>{errorTextPassword}</FormHelperText>
                </FormControl>
                <FormControl error={errorPassword}  sx={{ marginTop: 5 }}>
                    <InputLabel error={errorPassword} form='password'>Confirmar Senha:</InputLabel>
                    <Input error={errorPassword} type='password' placeholder='Confirme sua senha' value={confirmarSenha} onChange={(e) => setConfirmarSenha(e.target.value)}/>
                    <FormHelperText error={errorPassword}>{errorTextPassword}</FormHelperText>
                </FormControl>
                <Button onClick={handleSubmit} variant='contained' sx={{ marginTop: 3, marginLeft: 15, marginRight: 15 }}>Cadastrar</Button>
            </FormGroup>
        </Box>
        <p>Já possui uma conta? <Button href="/" variant='contained'>Login</Button></p>
    </Container>
  )
}

export default Cadastro