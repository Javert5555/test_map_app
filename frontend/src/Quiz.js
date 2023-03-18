import React, { useState } from "react";
import { TextField, Button, Grid, Paper } from '@material-ui/core';
import { makeStyles } from '@material-ui/core/styles';
import {Link, useHistory} from "react-router-dom";
import {useRecoilState} from 'recoil';
import {userState} from './state'

const useStyles = makeStyles({
    root: {
      background: '#fff',
      width: '40%',
      'min-width': '320px',
      'max-width': '475px',
      padding: '8px',
      position: 'relative',
      display: 'flex',
       'align-items': 'center',
        'justify-content': 'center',
    },
    button: {
        background: 'linear-gradient(45deg, #2CB0CE 30%, #539EFF 90%)',
        width:'50%',
        color: '#000'
        //position: 'absolute',
        //top: '70%',
    },
    input: {
        width: '100%',
        'padding-bottom': '8px'
    }
});

function Quiz() {
    const [title, setTitle] = useState("");
    const [content, setContent] = useState("");
    const classes = useStyles();
    let history = useHistory();

    function createQuiz(){
        // TODO
        fetch('/api/healthchecker', {
            method: 'GET',
            mode: 'cors',
            headers: {
              'Content-Type': 'application/json'
            }
        })
        .then(response => response.json())
        .then(data => {
            console.log('Success:', data);
        })
        .catch((error) => {
            console.error('Error:', error);
        });
        fetch('/api/quizzes', {
            method: 'POST',
            mode: 'cors',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({'title':title, 'content':content}) // body data type must match "Content-Type" header
        })
        .then(response => response.json())
        .then(data => {
            console.log('Success:', data);
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    }


    function handleSubmit(event) {
        event.preventDefault();
        createQuiz()
        console.log('title', title)
        console.log('content', content)
    }
    return (
    <Grid container direction="row" justify="center" alignItems="center" >
        <Paper className={classes.root}>
            <form onSubmit={handleSubmit}>
                <TextField className={classes.input} type='title' label="Title" variant="outlined" color="secondary" inputProps={{ 'aria-label': 'description' }} onChange={(e) => setTitle(e.target.value)}/>
                <TextField className={classes.input} type='content' label="Content" variant="outlined" color="secondary" inputProps={{ 'aria-label': 'description' }} onChange={(e) => setContent(e.target.value)}/>
                <Button className={classes.button} type="submit">Create quiz</Button>
            </form>
        </Paper>
    </Grid>    
    
    );
}

export default Quiz;