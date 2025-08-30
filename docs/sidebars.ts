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
      id: 'environment',
      label: 'Environment Configuration',
    },
    {
      type: 'doc',
      id: 'installation',
      label: 'Installation',
    },
    {
      type: 'category',
      label: 'APIReference',
      items: [
        {
          type: 'category',
          label: 'Mpesa Express',
          collapsed: true,
          items: [
            {
              type: 'doc',
              id: 'mpesa-express/stk-push',
              label: 'STK Push',
            },
            {
              type: 'doc',
              id: 'mpesa-express/stk-query',
              label: 'STK Query',
            },
          ],
        },
        {
          type: 'doc',
          id: 'dynamic-qr',
          label: 'Dynamic QR Code',
        },
        {
          type: 'doc',
          id: 'c2b',
          label: 'Customer to Business (C2B)',
        },
        {
          type: 'doc',
          id: 'b2c',
          label: 'Business to Customer (B2C)',
        },
      ],
    },
    {
      type: 'doc',
      id: 'webhooks-best-practices',
      label: 'Webhooks Best Practices',
    },
    {
      type: 'doc',
      id: 'example',
      label: 'Example',
    },
  ],
};

export default sidebars;