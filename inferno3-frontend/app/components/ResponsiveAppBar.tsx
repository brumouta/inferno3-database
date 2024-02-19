'use client'
import * as React from 'react';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import IconButton from '@mui/material/IconButton';
import Typography from '@mui/material/Typography';
import Menu from '@mui/material/Menu';
import MenuIcon from '@mui/icons-material/Menu';
import Container from '@mui/material/Container';
import MenuItem from '@mui/material/MenuItem';
import {Logo} from "@/components/Logo";
import config from "@/lib/config";
import {Divider, Link, Stack} from "@mui/material";

function ResponsiveAppBar() {
  const [anchorElNav, setAnchorElNav] = React.useState<null | HTMLElement>(null);

  const handleOpenNavMenu = (event: React.MouseEvent<HTMLElement>) => {
    setAnchorElNav(event.currentTarget);
  };

  const handleCloseNavMenu = () => {
    setAnchorElNav(null);
  };

  return (
      <AppBar position="static" sx={{backgroundColor: 'yellow'}}>
        <Container maxWidth="xl">
          <Toolbar disableGutters>
            <Logo/>
            <Typography
                variant="h6"
                noWrap
                component="a"
                href="/"
                sx={{
                  mr: 2,
                  display: {xs: 'none', md: 'flex'},
                  fontFamily: 'monospace',
                  fontWeight: 700,
                  letterSpacing: '.3rem',
                  color: 'red',
                  textDecoration: 'none',
                }}
            >
              I3DB
            </Typography>

            <Box sx={{flexGrow: 1, display: {xs: 'flex', md: 'none'}}}>
              <IconButton
                  size="large"
                  aria-label="account of current user"
                  aria-controls="menu-appbar"
                  aria-haspopup="true"
                  onClick={handleOpenNavMenu}
                  color="inherit"
              >
                <MenuIcon/>
              </IconButton>
              <Menu
                  id="menu-appbar"
                  anchorEl={anchorElNav}
                  anchorOrigin={{
                    vertical: 'bottom',
                    horizontal: 'left',
                  }}
                  keepMounted
                  transformOrigin={{
                    vertical: 'top',
                    horizontal: 'left',
                  }}
                  open={Boolean(anchorElNav)}
                  onClose={handleCloseNavMenu}
                  sx={{
                    display: {xs: 'block', md: 'none'},
                  }}
              >
                {config.nav.map((item) => (
                    <MenuItem key={item.name} onClick={handleCloseNavMenu}>
                      <Link
                          key={item.name}
                          underline={"none"}
                          onClick={handleCloseNavMenu}
                          sx={{
                            my: 2,
                            color: 'red',
                            display: 'block',
                            font: "monospace"
                          }}
                          href={item.path}
                      >
                        <Typography textAlign="center">{item.name}</Typography>
                      </Link>
                    </MenuItem>
                ))}
              </Menu>
            </Box>
            <Typography
                variant="h5"
                noWrap
                component="a"
                href="/"
                sx={{
                  mr: 2,
                  display: {xs: 'flex', md: 'none'},
                  flexGrow: 1,
                  fontFamily: 'monospace',
                  fontWeight: 700,
                  letterSpacing: '.3rem',
                  color: 'red',
                  textDecoration: 'none',
                }}
            >
              I3DB
            </Typography>
            <Box sx={{flexGrow: 1, display: {xs: 'none', md: 'flex'}}}>
              <Stack
                  direction="row"
                  divider={<Divider orientation="vertical" flexItem/>}
                  spacing={2}
              >
                {config.nav.map((item) => (
                    <Link
                        key={item.name}
                        underline={"none"}
                        onClick={handleCloseNavMenu}
                        sx={{
                          my: 2,
                          color: 'red',
                          display: 'block',
                          font: "monospace"
                        }}
                        href={item.path}
                    >
                      <Typography textAlign="center">{item.name}</Typography>
                    </Link>
                ))}
              </Stack>
            </Box>
          </Toolbar>
        </Container>
      </AppBar>
  );
}

export default ResponsiveAppBar;