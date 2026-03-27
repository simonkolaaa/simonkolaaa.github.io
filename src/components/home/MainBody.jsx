import React from "react";
import Container from "react-bootstrap/Container";
import { Jumbotron } from "./migration";

const MainBody = React.forwardRef(
  ({ gradient, title, message, icons }, ref) => {
    const [fontIndex, setFontIndex] = React.useState(0);
    const [msgIndex, setMsgIndex] = React.useState(0);
    const [isFade, setIsFade] = React.useState(false);

    const fonts = [
      "'Montserrat', sans-serif",
      "'Playfair Display', serif",
      "'Caveat', cursive",
      "'Orbitron', sans-serif",
      "'Dancing Script', cursive",
      "'Bebas Neue', cursive"
    ];

    React.useEffect(() => {
      const fontTimer = setInterval(() => {
        setIsFade(true);
        setTimeout(() => {
          setFontIndex((prev) => (prev + 1) % fonts.length);
          setMsgIndex((prev) => (prev + 1) % message.length);
          setIsFade(false);
        }, 500);
      }, 4000);

      return () => clearInterval(fontTimer);
    }, [fonts.length, message.length]);

    return (
      <Jumbotron
        fluid
        id="home"
        style={{
          background: `linear-gradient(136deg,${gradient})`,
          backgroundSize: "1200% 1200%",
        }}
        className="title bg-transparent bgstyle text-light min-vh-100 d-flex align-content-center align-items-center flex-wrap m-0"
      >
        <div id="stars"></div>
        <Container className="text-center">
          <h1 
            ref={ref} 
            className={`display-1 ${isFade ? 'text-fade-out' : 'text-fade-in'}`}
            style={{ fontFamily: fonts[fontIndex], transition: "all 0.5s ease-in-out" }}
          >
            {title}
          </h1>
          
          <div className={`lead typist ${isFade ? 'text-fade-out' : 'text-fade-in'}`} style={{ transition: "all 0.5s ease-in-out", minHeight: "1.5em" }}>
            {message[msgIndex]}
          </div>

          <div className="p-5">
            {icons.map((icon, index) => (
              <a
                key={`social-icon-${index}`}
                target="_blank"
                rel="noopener noreferrer"
                href={icon.url}
                aria-label={`My ${icon.image.split("-")[1]}`}
              >
                <i className={`fab ${icon.image}  fa-3x socialicons`} />
              </a>
            ))}
          </div>
          <a
            className="btn btn-outline-light btn-lg "
            href="#aboutme"
            role="button"
            aria-label="Learn more about me"
          >
            More about me
          </a>
        </Container>
      </Jumbotron>
    );
  }
);

export default MainBody;
