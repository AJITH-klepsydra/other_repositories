import Blogs from "./components/Blogs";
import Contact from "./components/Contact";
import Features from "./components/Features";
import Hero from "./components/Hero";

export default function Home() {
  return (
    <div >
      <Hero />
      <Features/>
      <Blogs/>
      <Contact/>
    </div>
  );
}
