import React, { Component } from "react";
import { render } from "react-dom";
import HomePage from "./HomePage";
import CreatePostPage from "./CreatePost";
import {
    BrowserRouter as Router,
    Switch,
    Route,
    Link,
    Redirect,
}from "react-router-dom";


export default class App extends Component{
    constructor(props){
        super(props);
    }
    render(){
        return(<Router>
                <Switch>
                    <Route exact path ='/'>This is the HomePage</Route>
                    <Route path ='/Post' component={CreatePostPage}/>
                </Switch>
            </Router>

        )
    }
}

const appDiv = document.getElementById("app")
render(<App name="bob" />, appDiv)
