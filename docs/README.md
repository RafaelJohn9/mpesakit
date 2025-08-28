# MpesaKit Landing Page Components

A collection of modular, reusable TSX components for building modern landing pages in Docusaurus, specifically designed for the MpesaKit Python M-Pesa SDK documentation site.

## Components Overview

### Core Components

1. **HeroSection** - Main landing section with title, description, badges, and CTAs
2. **StatsSection** - Statistics display with animated counters
3. **FeaturesSection** - Feature cards with icons and descriptions
4. **SecuritySection** - Security features with visual layers
5. **APIStatusSection** - Real-time API status monitoring
6. **DocumentationSection** - Documentation links and resources
7. **CTASection** - Call-to-action with installation instructions
8. **Footer** - Footer with links and social media
9. **MpesaKitLanding** - Complete landing page combining all components

## Installation

1. Copy the component files to your Docusaurus `src/components/` directory
2. Copy the CSS module to the same directory
3. Install any required dependencies (React is already included in Docusaurus)

```bash
src/
├── components/
│   ├── MpesaKit.module.css
│   ├── HeroSection.tsx
│   ├── StatsSection.tsx
│   ├── FeaturesSection.tsx
│   ├── SecuritySection.tsx
│   ├── APIStatusSection.tsx
│   ├── DocumentationSection.tsx
│   ├── CTASection.tsx
│   ├── Footer.tsx
│   ├── MpesaKitLanding.tsx
│   └── index.ts
```

## Usage

### Complete Landing Page

```tsx
import React from 'react';
import Layout from '@theme/Layout';
import { MpesaKitLanding } from '../components/MpesaKitLanding';

export default function Home(): JSX.Element {
  return (
    <Layout title="MpesaKit" description="Python M-Pesa SDK">
      <MpesaKitLanding />
    </Layout>
  );
}
```

### Individual Components

```tsx
import React from 'react';
import { HeroSection, StatsSection } from '../components';

const CustomPage: React.FC = () => {
  const heroData = {
    title: "Your Project",
    description: "Project description",
    badges: ["Feature 1", "Feature 2"],
    primaryCTA: { text: "Get Started", href: "/docs" },
    secondaryCTA: { text: "GitHub", href: "/github" }
  };

  const statsData = [
    { number: "99%", label: "Uptime" },
    { number: "1M+", label: "Downloads" }
  ];

  return (
    <>
      <HeroSection {...heroData} />
      <StatsSection stats={statsData} />
    </>
  );
};
```

## Component Props

### HeroSection

```typescript
interface HeroSectionProps {
  title: string;
  description: string;
  badges: string[];
  primaryCTA: { text: string; href: string };
  secondaryCTA: { text: string; href: string };
}
```

### StatsSection

```typescript
interface StatsSectionProps {
  stats: Array<{
    number: string;
    label: string;
  }>;
}
```

### FeaturesSection

```typescript
interface FeaturesSectionProps {
  title: string;
  subtitle: string;
  features: Array<{
    icon: string;
    title: string;
    description: string;
    features: string[];
  }>;
}
```

## Customization

### Colors and Themes

The components use CSS custom properties (variables) defined in the CSS module:

```css
:root {
  --mpesa-green: #00D13A;
  --mpesa-dark-green: #00B032;
  --mpesa-light-green: #4AE668;
  --dark-bg: #0a0a0a;
  --card-bg: rgba(255, 255, 255, 0.05);
  /* ... more variables */
}
```

To customize colors, modify these variables in your CSS or override them in your Docusaurus custom CSS.

### Responsive Design

All components are fully responsive with breakpoints at:

- 768px (tablet)
- 480px (mobile)

### Animations

Components include:

- Fade-in animations using Intersection Observer
- Slide-in animations for hero content
- Hover effects on cards and buttons
- Typewriter effect for code demo

## Features

- **Modular Design**: Use individual components or the complete landing page
- **TypeScript Support**: Full type definitions included
- **Responsive**: Works on all device sizes
- **Accessible**: Semantic HTML and proper contrast ratios
- **Performant**: Optimized animations and efficient rendering
- **Customizable**: Easy to modify colors, content, and layout

## Browser Support

- Chrome/Edge 90+
- Firefox 88+
- Safari 14+
- Mobile browsers with CSS Grid support

## Dependencies

- React 16.8+ (for hooks)
- CSS Grid and Flexbox support
- Intersection Observer API (polyfill available if needed)

## Best Practices

1. **Data Structure**: Keep component data in separate files or use a CMS
2. **Performance**: Use React.memo for components that don't change often
3. **Accessibility**: Test with screen readers and keyboard navigation
4. **SEO**: Ensure proper heading hierarchy and meta descriptions

## Troubleshooting

### Common Issues

1. **CSS not loading**: Ensure the CSS module is imported in your component
2. **Animations not working**: Check if Intersection Observer is supported
3. **Layout breaks**: Verify CSS Grid browser support

### Debug Mode

Add this to your CSS for debugging layout issues:

```css
.debug * {
  border: 1px solid red !important;
}
```

## Contributing

To modify these components:

1. Update the TypeScript interfaces in `types/index.ts`
2. Modify component logic in individual component files
3. Update styles in `MpesaKit.module.css`
4. Test responsiveness across devices
5. Update documentation

## License

These components are designed for the MpesaKit project and follow the same open-source license.
