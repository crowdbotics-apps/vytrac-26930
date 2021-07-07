import React, { Component, View } from 'react';
import Container from 'react-bootstrap/Container';
import Button from 'react-bootstrap/Button';
import Col from 'react-bootstrap/Col';
import Row from 'react-bootstrap/Row';
import '../../App.css';

import {store} from '../../util/store'

import loginBackground from '../../assets/images/login_background.png';
import poweredBy from '../../assets/images/powered_by.png';
import vytracWhite from '../../assets/images/vytrac_white.png';

class LoginForm extends Component {

  constructor(props) {
    store.init();
    super(props);
    this.state = {}
  }

  validate () {
    if (!this.state.username) {
      alert("Please fill your username");
      return false;
    } else if (!this.state.password) {
      alert("Please fill your password");
      return false;
    } else {
      return true;
    }
  }

  login() { 
    if(this.validate()) {
      try {
        /*store.data.login(this.state.username + '', this.state.password + '').then((result) => {
          if(result) {
            alert("Successful login!");
          } else {
            alert("Could not login");
          }
        });*/
        this.props.changeItem('login-token');
      } catch (ex) {
        alert("Could not login");
      }
    }
  }

  render() {
    return (
        <div> 
            <Row className="vertical-container">
                <Col style={{padding: 0, margin: 0}}>
                  <div className="green-line"></div>
                </Col>
                <Col style={{padding: 0, margin: 0}}>
                  <div className="grey-line"></div>
                </Col>
              </Row>  
              <p className="text-left">Welcome to <span className="bold-blue">VyTrac</span></p>

              <p className="text-left smaller-text">Lorem ipsum dolor sit amet, cons cdipiscing elit. Duis non turpis nec nunc </p>

              <p className="grey-text username-label">Username, Email or Phone number</p>
              <input onChange={(username) => this.setState({username: username})} className="text-field" type="text" name="username" />
              <input onChange={(password) => this.setState({password: password})} className="text-field" type="password" name="password" />

              <Row className="vertical-container remember-me">
                <Col style={{padding: 0, margin: 0}}  xs={1}>
                  <div className="greycheck" />
                </Col>
                <Col style={{padding: 0, margin: 0}}>
                  <span className="grey-text">&nbsp;&nbsp;&nbsp;&nbsp;Remember me</span>
                </Col>
              </Row>  

              <div className="login-bottom-buttons-container">
                <Button style={{marginRight: 50}} variant="light">FORGOT PASSWORD</Button>
                <Button onClick={() => this.login()}>LOGIN</Button>
              </div>
        </div>
    );
  }
}

export default LoginForm;