import React, { Component, View } from 'react';
import Container from 'react-bootstrap/Container';
import Button from 'react-bootstrap/Button';
import Col from 'react-bootstrap/Col';
import Row from 'react-bootstrap/Row';
import { withRouter } from "react-router-dom";

import '../../App.css';

import {store} from '../../util/store'

import LoginForm from './LoginForm';
import LoginToken from './LoginToken';
import ResetPassword from './ResetPassword';
import ResetPasswordInput from './ResetPasswordInput';

import loginBackground from '../../assets/images/login_background.png';
import poweredBy from '../../assets/images/powered_by.png';
import vytracWhite from '../../assets/images/vytrac_white.png';

class Login extends Component {

  constructor(props) {
    store.init();
    super(props);
    this.state = {
      currentItem: 'login'
    }
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
      } catch (ex) {
        alert("Could not login");
      }
    }
  }

  showItem() {
    if(this.state.currentItem == 'login') {
      return (
        <LoginForm changeItem={this.changeItem.bind(this)}></LoginForm>
      )
    } else if(this.state.currentItem == 'login-token') {
      return (
        <LoginToken changeItem={this.changeItem.bind(this)}></LoginToken>
      )
    } else if(this.state.currentItem == 'reset-password') {
      return (
        <ResetPassword changeItem={this.changeItem.bind(this)}></ResetPassword>
      )
    } else if(this.state.currentItem == 'reset-password-input') {
      return (
        <ResetPasswordInput changeItem={this.changeItem.bind(this)}></ResetPasswordInput>
      )
    } else {
      return (
        <LoginForm changeItem={this.changeItem.bind(this)}></LoginForm>
      );
    }
  }

  changeItem(item) {
    this.setState({currentItem: item})
  }

  render() {
    return (
      <Container className="login-container">
        <Row className="login-row">
          <Col className="login-background-image-gradient" xs={6}>
            <img className="login-background-image" src={loginBackground}></img>
            <div className="login-user-thumb"></div>
            <div className="logos-container">
              <img className="login-logo-top" src={poweredBy}></img>
              <img className="login-logo-bottom" src={vytracWhite}></img>
            </div>           
          </Col>
          <Col xs={5} className="login-form" xs={6}>
            {this.showItem()}
          </Col>
        </Row>
      </Container>
    );
  }
}

export default withRouter(Login);