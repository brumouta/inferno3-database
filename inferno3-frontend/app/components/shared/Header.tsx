import React from 'react';
import ResponsiveAppBar from "@/components/ResponsiveAppBar";

interface TopNavbarProps {
}

export default function Header() {
  return (
      <header>
        <ResponsiveAppBar />
      </header>
  )
}