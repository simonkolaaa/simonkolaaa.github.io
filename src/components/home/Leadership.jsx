```javascript
import React from "react";
import Carousel from "react-bootstrap/Carousel";
import { Jumbotron } from "./migration";
import { Row } from "react-bootstrap"; // Added Row import

const Leadership = ({ heading, message, img, imageSize }) => {
  return (
    <Jumbotron
      id="leadership"
      className="m-0"
      style={{ backgroundColor: "white" }}
    >
      <h2 className="display-4 pb-5 text-center">{heading}</h2>
      <div className="row justify-content-center">
        <div className="col-12 text-center">
          <p className="lead">{message}</p>
        </div>
        {img && img.length > 0 && (
          <div className="col-md-7">
            <Carousel>
              {img.map((value, index) => {
                return (
                  <Carousel.Item key={index}>
                    <img
                      className="d-block w-100"
                      src={value.img}
                      alt="First slide"
                      width={imageSize.width}
                      height={imageSize.height}
                    />
                    <Carousel.Caption>
                      <Row className="justify-content-center">
                        <h3>{value.label}</h3>
                      </Row>
                      <p>
                        {value.paragraph}
                      </p>
                    </Carousel.Caption>
                  </Carousel.Item>
                );
              })}
            </Carousel>
          </div>
        )}
      </div>
    </Jumbotron>
  );
};

export default Leadership;
