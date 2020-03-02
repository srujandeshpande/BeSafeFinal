import React, { Component } from 'react';
import ReactPageScroller from 'react-page-scroller';
import './Home.css';
import { Navbar, Nav, Container, Row, Col, Button, Pager, Pagination } from 'react-bootstrap';
import logo from './logo.png';
import { Link } from 'react-router-dom';

import HomepageIllustration from './Assets/homepageillustration.svg';
import CarCrashIcon from './Assets/carcrashicon.svg';
import ai1icon from './Assets/AI1icon.svg';
import ai2icon from './Assets/AI2.svg';
import mapimg from './Assets/map.svg';

import SignInSide from './SignInSide'
class Home extends Component {
    render() {
        return (
            <div>
              <SignInSide/>
            </div>
        );
    }
}

export default Home;
