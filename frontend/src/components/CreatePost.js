import React, { Component } from "react";
import Button from "@material-ui/core/Button";
import Grid from "@material-ui/core/Grid";
import Typography from "@material-ui/core/Typography";
import TextField from "@material-ui/core/TextField";
import FormHelperText from '@material-ui/core/FormHelperText';
import FormControl from "@material-ui/core/FormControl";;
import { Link } from "react-router-dom";
import Radio from '@material-ui/core/Radio'
import RadioGroup from "@material-ui/core/RadioGroup"
import FormControlLabel from "@material-ui/core/FormControlLabel"
import {FormLabel} from "@material-ui/core";


export default class CreatePostPage extends Component{

    constructor(props) {
        super(props);
        this.state = {
            name: "test"
        };
        this.handlePostButtonPressed = this.handlePostButtonPressed.bind(this)
    }
    handleNameChange(e){
        this.setState.name =  e.target.value
    }

    handlePostButtonPressed(){
        console.log(this.state);
    }
    render(){
        return(
        <Grid container spacing={1}>
            <Grid item xs={12} align="center">
                <Typography component={'h4'} variant={"h4"}>
                    Create a Post
                </Typography>
            </Grid>
            <Grid item xs={12} align="center">
                <FormControl component="fieldset">
                    <FormHelperText>
                            Guest control playback state
                    </FormHelperText>
                    {/*<RadioGroup row defaultValue="true">
                        <FormControlLabel value="true"
                                          control={<Radio color="primary"/>}
                                          label="Play/Pause"
                                          labelPlacement="bottom"/>
                        <FormControlLabel value="false"
                                          control={<Radio color="secondary"/>}
                                          label="no control"
                                          labelPlacement="bottom"/>
                    </RadioGroup>*/}
                </FormControl>
            </Grid>
            <Grid item xs={12} align="center">
                <FormControl>
                    <TextField required={true}
                                type="string"
                                onChange={this.handleNameChange}
                                inputProps={{
                                    style: {textAlign: "center"}
                                }}>
                        { this.state.value }
                    </TextField>
                                <FormHelperText>
                                       Post name
                                </FormHelperText>
                </FormControl>
            </Grid>
            <Grid  item xs={12} align="center">
                <Button
                        color="primary"
                        variant="contained"
                        onClick={this.handlePostButtonPressed}
                >
                    Create a Post
                </Button>
            </Grid>
            <Grid item xs={12} align="center">
                <Button color="secondary"
                        variant="contained"
                        to="/"
                        component={Link}
                >
                    Back
                </Button>
            </Grid>
        </Grid>
        )
    }
}