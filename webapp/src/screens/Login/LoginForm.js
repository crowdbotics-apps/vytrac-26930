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
        store.data.login(this.state.username + '', this.state.password + '').then((result) => {
          if(result) {
            alert("Successful login!");
          } else {
            alert("Could not login");
          }
        });
        //this.props.changeItem('login-token');
      } catch (ex) {
        alert("Could not login");
      }
    }
  }

  resetPassword() { 
    this.props.changeItem('reset-password');
  }

  render() {
    return (
        <div style={{height: '100%'}}> 
            <Row className="vertical-container">
              <Col className="line-container">
                <div className="green-line"></div>
              </Col>
              <Col className="line-container">
                <div className="grey-line"></div>
              </Col>
            </Row>  
            <p className="text-left">Welcome to <span className="bold-blue">VyTrac</span></p>

            <p className="text-left dynamic-font-normal">Lorem ipsum dolor sit amet, cons cdipiscing elit. Duis non turpis nec nunc </p>

            <p className="grey-text username-label dynamic-font-normal">Username, Email or Phone number</p>
            <input onChange={(username) => this.setState({username: username})} className="text-field" type="text" name="username" />
            <p className="grey-text password-label dynamic-font-normal">Password</p>
            <input onChange={(password) => this.setState({password: password})} className="text-field" type="password" name="password" />

            <Row className="vertical-container remember-me">
              <Col style={{padding: 0, margin: 0}}  xs={12}>
                <input type="checkbox" className="greycheck dynamic-font-normal" />
                <span className="grey-text dynamic-font-normal">&nbsp;&nbsp;&nbsp;&nbsp;Remember me</span>
              </Col>
            </Row> 

            <div style={{height: '35%'}}></div> 

            <Row>
              <Col xs={2}>
                <Button className="dynamic-font-normal" onClick={() => this.resetPassword()} style={{marginRight: '50%'}} variant="light">FORGOT PASSWORD</Button>
              </Col>
              <Col xs={8}>
              </Col>
              <Col xs={2}>
                <Button className="dynamic-font-normal" onClick={() => this.login()}>LOGIN</Button>
              </Col>
            </Row>
        </div>
    );
  }
}

export default LoginForm;