import {Stack} from '@mui/material';
import React from 'react';
import {Logo} from './Logo';

interface TopNavbarProps {
}

function TopNavbar() {
  return (
    <Stack
      direction="row"
      justifyContent="space-between"
      sx={{ width: '100%' }}
    >
      <Logo />
      <Stack direction='row' gap='24px'>
        {/*<Figlet text='Inferno3' />*/}
      </Stack>
    </Stack>
  );
}

export default TopNavbar;
