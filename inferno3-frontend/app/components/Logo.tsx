import Image from 'next/image';

import logo from '../icon.png'

function Logo() {
  return (
    <Image src={logo} alt="Inferno3 Database logo" />
  );
}

export { Logo };
