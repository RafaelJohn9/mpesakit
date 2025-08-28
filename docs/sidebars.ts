import type { SidebarsConfig } from '@docusaurus/plugin-content-docs';

const sidebars: SidebarsConfig = {
  tutorialSidebar: [
    {
      type: 'doc',
      id: 'intro',
      label: 'Introduction',
    },
    {
      type: 'doc',
      id: 'production',
      label: 'Production Requirements',
    },
    {
      type: 'doc',
      id: 'getting-credentials',
      label: 'Getting Credentials',
    },
    {
      type: 'doc',
      id: 'example',
      label: 'Example',
    },

  ],
};

export default sidebars;