import React from 'react'
import { Box, Button, Container, FormControl,FormControlLabel, FormGroup, InputLabel, Radio, RadioGroup } from '@mui/material'

const Solicitacao = () => {
    const updatedJSON = {
        "nome": "Adriana",
        "tipo": "Area de RH",
        "gravidade": "Urgente",
        "descricao": "Extrema Urgencia"
    }

    const updateJson = () => {
        fs.writeFile('../public/data.json', JSON.stringify(updatedJSON), (err) => {
            if (err) console.log('Error writing file:', err);
        })
    }

  return (
    <Container  sx={{ 
        display: 'flex', 
        flexDirection: 'column', 
        textAlign: 'center', 
        justifyContent: 'center', 
        alignItems: 'center',
        padding: 5 
    }}>
        <h1>Solicitação</h1>
        <Box sx={{ display: 'flex', flexDirection: 'column', width: 600, backgroundColor: 'white', padding: 5 }}>
            <FormGroup>
                <FormControl>
                    <p>Por favor selecione a sua solicitação</p>
                    <RadioGroup sx={{ display: 'grid', gridTemplateColumns: 'auto auto auto' }}>
                        <FormControlLabel value="1" control={<Radio />} label="Area de TI" />
                        <FormControlLabel value="2" control={<Radio />} label="Area de RH" />
                        <FormControlLabel value="3" control={<Radio />} label="Setor Comerial" />
                        <FormControlLabel value="4" control={<Radio />} label="Area de Gerenciamento" />
                        <FormControlLabel value="5" control={<Radio />} label="Area Fiscal" />
                        <FormControlLabel value="6" control={<Radio />} label="Area de Marketing" />
                    </RadioGroup>
                </FormControl>
                <FormControl>
                    <p>Por favor descreva a natureza de sua solicitação:</p>
                    <textarea />
                </FormControl>
                <FormControl>
                    <p>Por favor indique o nivel de gravidade de sua solicitação:</p>
                    <RadioGroup>
                    <FormControlLabel value="1" control={<Radio />} label="Pequena Urgencia" />
                        <FormControlLabel value="2" control={<Radio />} label="Urgencia Moderada" />
                        <FormControlLabel value="3" control={<Radio />} label="Urgente" />
                        <FormControlLabel value="4" control={<Radio />} label="Extrema Urgencia" />
                    </RadioGroup>
                </FormControl>
                <Button onClick={updateJson} href='/dashboard' variant='contained' sx={{ marginX:20 }}>Solicitar</Button>
            </FormGroup>
        </Box>
    </Container>
  )
}

export default Solicitacao